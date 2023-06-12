#
# app styles static objects
#

COLORS = {
    "c1": "#ebf7ff",
    "white": "#F5FFFA",
    "darkBlue": "#033454",
    "main_app_page_background": "#f1f7fd"
}

MAIN_APP_PAGE_BACKGROUND = "#f1f7fd"

#
# main.py
#
APP_TOP_MARGIN = {
    'backgroundColor': '#033454',
    'text': '#F5FFFA',
    'text-align': 'center'}

SIDEBAR_DIVIDER_STYLE = {
    'size': 45,
    'marginBottom': 5,
    'marginTop': 10}

theme_icons = {
    'left': 'fa fa-sun',
    'right': 'fa fa-moon'}

NAV_LINK_THEME_ICON = {
    'DashIconify_width': 40,
    'size': 30,
    'radius': 90,
    'variant': 'light'  # ["filled","light","gradient","outline"].
}

NAV_LINK_STYLE = {
    'textDecoration': 'none',
    'backgroundColor': MAIN_APP_PAGE_BACKGROUND
}

LOGO_NAME = 'img_2'

DEFAULT_COMPONENT_CENTER = {
    'textAlign': 'center',
    'backgroundColor': MAIN_APP_PAGE_BACKGROUND,
    # 'borderRadius': '5px',
}

MAIN_3D_LAYOUT_STYLE = {
    'textAlign': 'center',
    'marginLeft': '8%'
}

# -----------------------------------------------MAIN PAGE GADGETS------------------------------------------------

SIDE_BUTTON_STYLE = {
    'size': '33',
    'marginTop': '60%',
    'borderRadius': '30%',
    'textAlign': 'center',
    'width': '49%',
    'height': '15%',
    'color': '#FFFFFF',
    'marginLeft': '1%',
    'variant': 'light'
}

BUTTON_STYLE = {
    'size': '30',
    'borderRadius': '30%',
    'width': '20%',
    'height': '5%',
    'textColor': '#FFFFFF',
    'marginLeft': '0%',
    'backgroundColor': '#ebf7ff',
}


BUTTON_STYLE_REF = {
    'size': '90000',
    'borderRadius': '50%',
    'width': '10%',
    'height': '100px',
    'marginLeft': '60%',
    'backgroundColor': '#ebf7ff',
    'border': '1px solid black',
    'transition': 'background-color 0.5s ease',
    ':hover': {
        'backgroundColor': '#d6e9ff',
    }
}


SIDEBAR_STYLE = {
    'backgroundColor': '#e2f0f9'
}

MAIN_APP_STYLE = {
    'backgroundColor': MAIN_APP_PAGE_BACKGROUND,
    'height': 1080
}

MAIN_LAYOUT_STYLE = {
    'backgroundColor': MAIN_APP_PAGE_BACKGROUND,
    'size': 'xl',
    'fontSize': 18,
    'textAlign': 'left'}

APP_HEADERS_STYLE = {
    'backgroundColor': MAIN_APP_PAGE_BACKGROUND,
    'size': 'xl',
    'fontSize': 18,
    'textAlign': 'center'
}

LAYOUT_CONTENT_STYLE = {
    'size': 'lg',  # Size of the page
    'marginLeft': '16%',  # Where the main layout start (from the side)
    'marginTop': '0%',  # Where the main layout start (from the top)
    'fontSize': 17,  # Size of the font in all pages!
    'backgroundColor': MAIN_APP_PAGE_BACKGROUND,
}
MAIN_SIDE_BAR = {
    'Location': {'top': 30, 'left': 0},
    'Base': {'base': '20%'}
}
DATATABLE_HEADER_STYLE = {
    'backgroundColor': 'white',
    'textAlign': 'center',
    'fontWeight': 'bold'
}

USER_BOX_DATATABLE_STYLE = {
    'whiteSpace': 'normal',
    'height': 'auto',
    'width': 'auto',
    'minxWidth': '30px',
    'maxWidth': '30px',
    'maxHeight': '30px',
}

STYLE_TABLE_BOX = {
    'maxHeight': '2000px',
    'overflowY': 'hidden',
    'overflowX': 'auto',
    'maxWidth': '80%',
    'paddingBottom': 200
}

DROP_FILES_AREA_STYLE = {'width': '50%',
                         'height': '60px',
                         'lineHeight': '60px',
                         'borderWidth': '1px',
                         'borderStyle': 'dashed',
                         'borderRadius': '5px',
                         'textAlign': 'center',
                         'marginLeft': '15%'}

# --------------------------------------------- 3D GRAPH LEGEND STYLING --------------------------------------------


LEGEND_DIV_WRAPPER = {
    'textAlign': 'center',
    'marginLeft': '15%',
    'display': 'grid',
    'gridTemplateColumns': 'repeat(auto-fit, minmax(10%, 1fr))',
    'justifyContents': 'center',
    'alignItems': 'center',
    'width': 1200,
    'padding': '10px 0',
    'marginTop': '30px',
    'backgroundColor': MAIN_APP_PAGE_BACKGROUND,
}

LEGEND_COLOR = {
    'width': '1rem',
    'height': '1rem',
    'border': '1px solid black'
}

LEGEND_ITEM_WRAPPER = {
    'margin': 'auto',
    'width': 'auto',
    'textAlign': 'center',
    'display': 'flex',
    'gap': 10,
    'justifyContents': 'center',
    'alignItems': 'center',
    'backgroundColor': MAIN_APP_PAGE_BACKGROUND,
}
