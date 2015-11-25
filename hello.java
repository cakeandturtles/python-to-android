package com.example.helloworld;

import android.app.Activity;
import android.os.Bundle;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends Activity {
	
	public static LinearLayout mainLayout(Activity activity){
		LinearLayout layout = new LinearLayout(activity);
		layout.setOrientation(LinearLayout.VERTICAL);
		
		TextView text = new TextView(activity);
		text.setText("Hello, world!");
		layout.addView(text);
		
		return layout;
	}

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(mainLayout(this));
		
		Toast toast = Toast.makeText(getApplicationContext(), "Goodbye, world!", Toast.LENGTH_LONG);
		toast.show();
	}
}