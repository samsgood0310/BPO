import dash
import dash_mantine_components as dmc
from dash import dcc, html
from dash_iconify import DashIconify

from app.assets import style_consts
from app.utils.common_functions import get_picture


def create_nav_link(icon, label, href) -> dcc.Link:
    """
    This function create a Nav link format using when given the icon / label / herf parameters
    """
    return dcc.Link(
        dmc.Group(
            [
                dmc.ThemeIcon(
                    DashIconify(
                        icon=icon,
                        width=style_consts.NAV_LINK_THEME_ICON.get('DashIconify_width')),
                    size=style_consts.NAV_LINK_THEME_ICON.get('size'),
                    radius=style_consts.NAV_LINK_THEME_ICON.get('radius'),
                    variant=style_consts.NAV_LINK_THEME_ICON.get('variant'),
                ),
                dmc.Text(
                    label,
                    size='lg',
                    color='dimmed',
                    weight='bolder'
                ),
            ]),
        href=href,
        style=style_consts.NAV_LINK_STYLE,
    )


def get_sidebar():
    return dmc.Navbar(
        fixed=True,
        width=style_consts.MAIN_SIDE_BAR.get('Base'),
        position=style_consts.MAIN_SIDE_BAR.get('Location'),
        pl='1%',
        height=1080,
        style=style_consts.SIDEBAR_STYLE,
        children=[
            html.A(
                href='/',
                children=[
                    html.Img(
                        src=get_picture("main_logo"), height='100%', width='100%'
                    )
                ]
            ),
            dmc.Group(
                grow=True,
                direction='column',
            ),
            dmc.ScrollArea(
                offsetScrollbars=True,
                type='scroll',
                children=[
                    dmc.Group(
                        direction='column',
                        children=[
                            create_nav_link(
                                icon='clarity:home-line',
                                label='Welcome Page',
                                href='/',
                            ),
                        ],
                    ),
                    dmc.Divider(
                        label='Problem Definition', style=style_consts.SIDEBAR_DIVIDER_STYLE
                    ),
                    dmc.Group(
                        direction='column',
                        children=[
                            create_nav_link(
                                icon=page['icon'], label=page['name'], href=page['path']
                            )
                            for page in dash.page_registry.values()
                            if page['path'].startswith('/definition')
                        ],
                    ),
                    dmc.Divider(
                        label='Solution Presenting', style=style_consts.SIDEBAR_DIVIDER_STYLE
                    ),
                    dmc.Group(
                        direction='column',
                        children=[
                            create_nav_link(
                                icon=page['icon'], label=page['name'], href=page['path']
                            )
                            for page in dash.page_registry.values()
                            if page['path'].startswith('/solution')
                        ],
                    ),
                ],
            ),
            html.Div([
                dmc.Button(
                    html.A('Source Code', href='https://github.com/Asaf95', target='_blank'),
                    leftIcon=[DashIconify(icon='line-md:github', width=36)],
                    style=style_consts.SIDE_BUTTON_STYLE
                ),
                dmc.Button(
                    html.A(
                        'Contact Me', href='https://www.linkedin.com/in/asafbm/', target='_blank'),
                    leftIcon=[DashIconify(icon='line-md:linkedin', width=36)],
                    style=style_consts.SIDE_BUTTON_STYLE
                ),
            ]
            ),
            dmc.Space(h=10),
            dmc.Text('© GNU - Free Software Foundation', align='center'),
            dmc.Space(h=5),
        ],
    )
