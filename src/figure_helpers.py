import numpy as np
def polynomial_function(x, *coefficients):
    degree = len(coefficients) - 1
    y = np.zeros_like(x)
    for i, coeff in enumerate(coefficients):
        y += coeff * x**(degree - i)
    return y

def rotate_point(x, y, angle_rad):
    cos, sin = np.cos(angle_rad), np.sin(angle_rad)
    return cos * x - sin * y, sin * x + cos * y

def draw_brace(ax, span, position, text, text_pos, brace_scale=1.0, beta_scale=5.0, rotate=False, rotate_text=False):
    '''
        all positions and sizes are in axes units
        span: size of the curl
        position: placement of the tip of the curl
        text: label to place somewhere
        text_pos: position for the label
        beta_scale: scaling for the curl, higher makes a smaller radius
        rotate: true rotates to place the curl vertically
        rotate_text: true rotates the text vertically
    '''
    ax_xmin, ax_xmax = ax.get_xlim()
    xax_span = ax_xmax - ax_xmin
    resolution = int(span / xax_span * 500) * 2 + 1  # increased resolution for smoother curve
    beta = beta_scale / xax_span  # the higher this is, the smaller the radius
    x = np.linspace(-span / 2., span / 2., resolution)
    x_half = x[:int(resolution / 2) + 1]
    y_half_brace = (1 / (1. + np.exp(-beta * (x_half - x_half[0])))
                    + 1 / (1. + np.exp(-beta * (x_half - x_half[-1]))))
    y = np.concatenate((y_half_brace, y_half_brace[-2::-1]))
    max_y = np.max(y)
    min_y = np.min(y)
    y /= (max_y - min_y)
    y *= brace_scale
    y -= max_y
    if rotate:
        x, y = rotate_point(x, y, -np.pi / 2)
    x += position[0]
    y += position[1]
    ax.autoscale(False)
    ax.plot(x, y, color='black', lw=1, clip_on=False)
    ax.text(text_pos[0], text_pos[1], text, ha='center', fontsize=11,
            va='bottom', rotation=90 if rotate_text else 0)