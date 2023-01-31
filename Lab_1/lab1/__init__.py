import scipy.io as sio
import numpy as np
import svm

def main():
    # Исследование линейного ядра
    data = {}
    sio.loadmat('/Volumes/data/workspace/Python/machineLearningCource/Lab_1/lab1/dataset1.mat', data)

    X = data['X']
    y = data['y']

    y = y.astype(np.float64)

    # 1
    svm.visualize_boundary_linear(X, y, None, 'Исходные данные')

    # 2
    C = 1
    model = svm.svm_train(X, y, C, svm.linear_kernel, 0.001, 20)
    svm.visualize_boundary_linear(X, y, model, 'Разделяющая граница при C=1')

    # 3
    C = 100
    model = svm.svm_train(X, y, C, svm.linear_kernel, 0.001, 20)
    svm.visualize_boundary_linear(X, y, model, 'Разделяющая граница при C=100')

    # Исследование гауссова ядра
    # 4
    svm.contour(1)
    svm.contour(3)

    # 5
    data = {}
    sio.loadmat('/Volumes/data/workspace/Python/machineLearningCource/Lab_1/lab1/dataset2.mat', data)

    X = data['X']
    y = data['y']

    y = y.astype(np.float64)

    svm.visualize_boundary_linear(X, y, None, 'Исходные данные')

    # 6
    C = 1.0
    sigma = 0.1
    gaussian = svm.partial(svm.gaussian_kernel, sigma=sigma)
    gaussian.__name__ = svm.gaussian_kernel.__name__
    model = svm.svm_train(X, y, C, gaussian)
    svm.visualize_boundary(X, y, model, 'Использование гауссова ядра')

    # 7
    data = {}
    sio.loadmat('/Volumes/data/workspace/Python/machineLearningCource/Lab_1/lab1/dataset3.mat', data)

    X = data['X']
    y = data['y']
    Xval = data['Xval']
    yval = data['yval']

    y = y.astype(np.float64)

    # svm.visualize_boundary_linear(X, y, None, 'Обучающая выборка')
    # svm.visualize_boundary_linear(Xval, yval, None, 'Тестовая выборка')

    # 8
    C = 1
    sigma = 0.5
    gaussian = svm.partial(svm.gaussian_kernel, sigma=sigma)
    gaussian.__name__ = svm.gaussian_kernel.__name__
    model = svm.svm_train(X, y, C, gaussian)
    svm.visualize_boundary(X, y, model, 'Модель при неоптимальных параметрах С = %f, sigma= %f' % (C, sigma) )

    # 9
    minError = 100
    for C in [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]:
        for sigma in [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]:
            gaussian = svm.partial(svm.gaussian_kernel, sigma=sigma)
            gaussian.__name__ = svm.gaussian_kernel.__name__
            model = svm.svm_train(X, y, C, gaussian)
            ypred = svm.svm_predict(model, Xval)
            error = np.mean(ypred != yval.ravel())
            if error < minError :
                minC = C
                minSigma = sigma
                minError = error


    gaussian = svm.partial(svm.gaussian_kernel, sigma=minSigma)
    gaussian.__name__ = svm.gaussian_kernel.__name__
    model = svm.svm_train(X, y, minC, gaussian)

    svm.visualize_boundary(X, y, model, 'Наилучшая модель для обучающей выборки при C = %f, sigma = %f' % (minC, minSigma))
    svm.visualize_boundary(Xval, yval, model, 'Наилучшая модель для тестовой выборки при C=  %f, sigma = %f' % (minC, minSigma))

if __name__ == '__main__':
    main()
