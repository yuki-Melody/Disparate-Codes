# PRF in keras caculated by epoch-wise, use sklearn.metrics

import numpy
from keras.callbacks import Callback
from sklearn.metrics import f1_score, precision_score, recall_score


class Metrics(Callback):
    def on_train_begin(self, logs={}):
        self.val_f1s = []
        self.val_recalls = []
        self.val_precisions = []

    def on_epoch_end(self, epoch, logs={}):
#         print(len(self.validation_data),(self.validation_data[59]))
        val_predict = (numpy.asarray(self.model.predict(
            self.validation_data[0:59]))).round()  #round()四舍五入
#         print(val_predict)
        val_predict = [1 if list(i)==[1.,0.] else 0 for i in val_predict]
        val_targ = [1 if list(i)==[1.,0.] else 0 for i in self.validation_data[59]]
        _val_f1 = f1_score(val_targ, val_predict)
        _val_recall = recall_score(val_targ, val_predict)
        _val_precision = precision_score(val_targ, val_predict)
        self.val_f1s.append(_val_f1)
        self.val_recalls.append(_val_recall)
        self.val_precisions.append(_val_precision)
        print('val_precision{0};val_recall{1};val_f-score{2}'.format(self.val_precisions, self.val_recalls, self.val_f1s))
        return
metrics = Metrics()
