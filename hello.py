from android import Activity, LinearLayout, TextView, Toast

class MainActivity(Activity):
    def mainLayout(self):
        layout = LinearLayout(self)
        layout.orientation = LinearLayout.VERTICAL
        
        text = TextView(self)
        text.text = "Hello, world!"
        layout.addView(text)
        
        return layout

    def onCreate(self, savedInstanceState):
        super(MainActivity, self).onCreate(savedInstanceState)
        setContentView(mainLayout(self))
        
        toast = Toast.makeText("Goodbye, world!")
        toast.show()