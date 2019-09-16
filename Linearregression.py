import numpy as np
X=np.array([1,2,3,4,5,6,7,8,9])
y=np.array([5,5,6,7,8,8,9,9,9])
def linear_regression (X, y, m_current=0, b_current=0, epochs=1000, learning_rate=0.0001):
    N=float(len(y))
    for i in range(epochs):
        y_current=(m_current*X)+b_current
        cost=sum([data**2 for data in (y-y_current)])/N
        m_gradient=-(2/N)*sum(X*(y-y_current))
        b_gradient=-(2/N)*sum(y-y_current)
        m_current=m_current-(learning_rate*m_gradient)
        b_current=b_current-(learning_rate*b_gradient)
        print (m_current, b_current, cost)
    return m_current, b_current, cost
linear_regression(X, y)
    