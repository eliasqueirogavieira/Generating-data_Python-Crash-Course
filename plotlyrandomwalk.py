import plotly.graph_objs as go
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk using plotly.
    point_numbers = list(range(rw.num_points))
    fig = go.Figure()

    # Add the main scatter plot
    fig.add_trace(go.Scatter(x=rw.x_values, y=rw.y_values, mode='markers',
                             marker=dict(size=8, color=point_numbers, colorscale='Viridis', showscale=False)))

    # Emphasize the first and last points.
    fig.add_trace(go.Scatter(x=[rw.x_values[0], rw.x_values[-1]],
                             y=[rw.y_values[0], rw.y_values[-1]], mode='markers',
                             marker=dict(size=15, color=['red', 'blue'], showscale=False)))

    # Remove the axes.
    fig.update_xaxes(visible=False, showticklabels=False)
    fig.update_yaxes(visible=False, showticklabels=False)

    fig.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break
