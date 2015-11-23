from android import Activity, LinearLayout, TextView, Toast

def mainLayout(activity):
    layout = LinearLayout()
    layout.orientation = "vertical"
    
    text = TextView()
    text.text = "Hello, world!"
    layout.addChild(text)
    
    return layout

class MainActivity(Activity):
    def onCreate(self, savedInstanceState):
        super(MainActivity, self).onCreate(savedInstanceState)
        setContentView(mainLayout(self))
        
        toast = Toast.makeText("Goodbye, world!")
        toast.show()