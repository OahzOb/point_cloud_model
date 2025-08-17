import numpy as np
import plotly.graph_objects as go
from vispy import app, scene
from vispy.color import Colormap


def try_vispy():
    # 创建100万个随机点
    points = np.random.randn(1000000, 3)
    colors = np.random.rand(1000000, 4)  # RGBA颜色

    # 创建画布和视图
    canvas = scene.SceneCanvas(keys='interactive', show=True)
    view = canvas.central_widget.add_view()
    view.camera = 'turntable'  # 使用旋转相机
    view.camera.fov = 45  # 视野角度
    view.camera.distance = 10  # 相机距离

    # 创建点云
    scatter = scene.visuals.Markers()
    scatter.set_data(points, edge_color=None, face_color=colors, size=3, symbol='o')
    view.add(scatter)

    # 添加坐标轴
    axis = scene.visuals.XYZAxis(parent=view.scene)

    # 运行应用
    app.run()


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


# if __name__ == '__main__':
    # try_go()
    # try_vispy()
canvas = scene.SceneCanvas(keys='interactive', show=True)
view = canvas.central_widget.add_view()
view.camera = scene.TurntableCamera(distance=5)

# 创建初始对象
points = np.array([[0, 0, 0]])
scatter = scene.visuals.Markers(pos=points, size=10, face_color='red')
view.add(scatter)

# 动画状态
angle = 0


# 更新函数
def update(event):
    global angle
    angle += 0.05

    # 计算新位置
    x = np.cos(angle) * 2
    y = np.sin(angle) * 2
    z = np.sin(angle * 2)

    # 更新点位置
    scatter.set_data(pos=np.array([[x, y, z]]))

    # 更新视图
    canvas.update()


# 创建定时器
timer = app.Timer(interval=0.016, connect=update, start=True)  # ~60 FPS

app.run()