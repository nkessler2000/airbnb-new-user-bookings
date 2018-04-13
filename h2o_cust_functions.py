def perf_to_cm_array(perf):
    """Takes an h2o model performance object and returns a numpy array
	with the confusion matrix)"""
    cm_df = perf.confusion_matrix().as_data_frame()
    n_classes = len(cm_df) - 1
    return np.array(cm_df.iloc[:n_classes, :n_classes])
