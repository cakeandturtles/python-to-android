from android import Activity, LinearLayout, TextView, Toast

def mainLayout(activity):
    layout = LinearLayout(activity)
    layout.orientation = LinearLayout.VERTICAL
    
    text = TextView(activity)
    text.text = "Hello, world!"
    layout.addView(text)
    
    return layout

class MainActivity(Activity):
    def onCreate(self, savedInstanceState):
        super(MainActivity, self).onCreate(savedInstanceState)
        setContentView(mainLayout(self))
        
        toast = Toast.makeText("Goodbye, world!")
        toast.show()