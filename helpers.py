kv2="""
<Controller>
    label_wid: custom_label
    textfield: question
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
                ScrollView:
                    do_scroll_x:False
                    do_scroll_y:True
                    MDLabel:
                        id:custom_label
                        text: "nice"*10000
                MDTextField:
                    id:question
                    hint_text: "Type here"
                    pos_hint:{'center_x': 0.5}
                    size_hint_x:None
                    width:200
                MDIconButton:
                    icon:"chevron-double-right"
                    pos_hint:{'center_x': 0.9, 'center_y': 0.05}
                    on_press: root.doThis(question.text)
                    on_release: root.clearField()


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
                    width:300
                    text: 'Made by Aashi Ranawat and Fahad Khan, special thanks to Ms. Chetna Singh for guiding us throughout the project.'
                    halign: 'center'
"""

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
                id:custom_label
                width:250
                pos_hint:{'center_x': 0.5,'center_y':0.5}
                size_hint_x:None
                text: "Here goes answer"


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
                width:300
                text: 'Static text, github link, somaiya IDs etc'
                halign: 'center'
"""


kv1="""
<Controller>
    label_wid: custom_label
    textfield: question
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
                    width:200
                MDIconButton:
                    icon:"chevron-double-right"
                    pos_hint:{'center_x': 0.9, 'center_y': 0.05}
                    on_press: root.doThis(question.text)
                    on_release: root.clearField()
                MDLabel:
                    id:custom_label
                    width:200
                    pos_hint:{'center_x': 0.5,'center_y':0.5}
                    size_hint_x:None
                    text: ""


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
                    width:300
                    text: 'Made by Aashi Ranawat and Fahad Khan, special thanks to Ms. Chetna Singh for guiding us throughout the project.'
                    halign: 'center'
"""
kv3="""
ScrollView:
    do_scroll_x: False
    do_scroll_y: True

    Label:
        size_hint_y: None
        height: self.texture_size[1]
        padding: 10, 10
        text:'really some amazing text'*100
"""
