textfield= """
MDTextField:
    hint_text: "Type here"
    pos_hint:{'center_x': 0.5}
    size_hint_x:None
    width:300
"""


kv="""
BoxLayout:
    orientation:'vertical'
    MDToolbar:
        title: 'Project C0VID-19'
        md_bg_color: .2, .2, .2, 1
        specific_text_color: 1, 1, 1, 1
    MDBottomNavigation:
        panel_color: .2, .2, .2, 1
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Bot'
            icon:'android-debug-bridge'
            MDTextField:
                id:question
                hint_text: "Type here"
                pos_hint:{'center_x': 0.5}
                size_hint_x:None
                width:250
            MDIconButton:
                icon:"chevron-double-right"
                pos_hint:{'center_x': 0.9, 'center_y': 0.05}
                on_press: app.doThis(question.text)
            MDLabel:
                text: app.doThis(question.text)
                pos_hint:{'center_x':0.5, 'center_y': 0.5}


        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Zones'
            icon:'map-marker-outline'
            MDLabel:
                text: 'Screen two'
                halign: 'center'
        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'About us'
            icon:'bat'
            MDLabel:
                text: 'A project by me'
                halign: 'center'
"""
