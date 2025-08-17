import numpy as np
import plotly.graph_objects as go


def try_go():
    x = np.linspace(-10, 10, 200)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_tan = np.tan(x)

    fig = go.Figure()

    fig.add_trace(
        go.Scattergl(
            x=x,
            y=y_sin,
            name='Sine Wave',
            line=dict(color='firebrick', width=3, dash='solid'),
            mode='lines'
        )
    )
    fig.add_trace(
        go.Scattergl(
            x=x,
            y=y_cos,
            name='Cosine Wave',
            line=dict(color='royalblue', width=3, dash='dashdot'),
            mode='lines+markers',
            marker=dict(size=4, symbol='diamond')
        )
    )
    fig.add_trace(
        go.Scattergl(
            x=x,
            y=y_tan,
            name='Tangent Wave',
            line=dict(color='forestgreen', width=2, dash='dot'),
            opacity=0.8,
        )
    )
    fig.update_layout(
        title='graph_objects test',
        xaxis_title='Radians',
        yaxis_title='Magnitude',
        xaxis_range=[-10, 10],
        yaxis_range=[-10, 10],
        legend_title='Wave type'
    )

    fig.show(renderer='browser')


if __name__ == '__main__':
    try_go()
