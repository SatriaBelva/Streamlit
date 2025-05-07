def hide_tools() :
    style = '''
    <style>
        [data-testid='stMainBlockContainer']{
            padding-left:0px; 
            padding-right:0px; 
            padding-top:0px;
        }
        [data-testid='stHeader']{
            display: none;
        }
    </style>
    </style>'''
    return style