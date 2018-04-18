package com.cdam.tp3;

import android.app.Activity;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.Toast;

public class EditeurTodo extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Intent intent;

    }

    public void onAnnulerClick(View v) {
        // A la fin : Réponse de fin ok
        Intent intent;
        intent = new Intent(this, AfficheurTodo.class);
        setResult(Activity.RESULT_CANCELED, intent);
        this.finish();
    }

    public void onOkClick(View v) {
        // A la fin : Réponse de fin ok
        Intent intent;
        intent = new Intent(this, AfficheurTodo.class);
        setResult(Activity.RESULT_OK, intent);
        this.finish();
    }
    public void RecupDate(View v){
        String res ="";
        EditText titre = findViewById(R.id.titre);
        String tit = titre.getText().toString();
        DatePicker dp = findViewById(R.id.date) ;
        String jour = "" + dp.getDayOfMonth();
        String moi = "" + dp.getMonth();
        String ann = "" + dp.getYear();
        res=res+jour+"/"+moi+"/"+ann;
        Toast.makeText(getApplicationContext(), tit+" "+res,
                Toast.LENGTH_SHORT).show();

    }
}
