kv1="""
<Controller>
    label_wid: custom_label
    textf: question
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
                ScrollView:
                    do_scroll_x: False
                    do_scroll_y: True
                    width:200
                    pos_hint:{'center_x': 0.5,'center_y':0.5}
                    size_hint_x:None
                    size_hint_y:0.8
                    scroll_y: 0
                    MDLabel:
                        id:custom_label
                        text: ""
                        size_hint: 1, None
                        size: self.texture_size

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
                    width:200
                    text: 'Made by Aashi Ranawat and Fahad Khan, special thanks to Ms. Chetna Singh for guiding us throughout the project.'
                    halign: 'center'
"""
