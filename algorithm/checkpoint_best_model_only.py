# only save the model of lowest val_loss score

from keras.callbacks import Callback
class save_optimal_model(Callback):
    def __init__(self, filepath):
        self.filepath = filepath
        self.val_loss_dict = {} 
    def get_model_path(e,v):
        return os.path.join(
            self.filepath,
            'model_{epoch:02d}-{val_loss:.4f}.hdf5'.format_map({
                'epoch':e,
                'val_loss':v
            })
        )
    def on_epoch_end(self, epoch, logs={}):      
        if epoch == 0:  
            self.val_loss = logs['val_loss']
            self.model.save(self.get_model_path(epoch, self.val_loss), overwrite=True)
            self.val_loss_dict[epoch] = self.val_loss
        else:
            keys = list(self.val_loss.keys())
            tmp_epoch = keys[-1]
            tmp_val_loss = self.val_loss_dict[tmp_epoch]
            if self.val_loss < tmp_val_loss:
                os.remove(self.get_model_path(tmp_epoch, tmp_val_loss))
                self.model.save(self.get_model_path(epoch, self.val_loss), overwrite=True)
                self.val_loss_dict[epoch] = self.val_loss
            else:
                pass