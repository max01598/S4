package com.cdam.tp3;


import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Locale;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.TextView;
import android.widget.Toast;
import java.util.Locale;

public class AfficheurTodo extends AppCompatActivity implements OnClickListener {

        private Date d;

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_afficheur_todo);


            // Récupérer l'intent requête
            Intent i;
            i = this.getIntent();

            // Récupérer les datas sur lesquelles travailler
            // l'Id de Todo
            int taskid = i.getIntExtra("TODO_ID", -1);
            if (taskid == -1) {
                // Si pas de Todo : Réponse de fin cancel
                Toast.makeText(getApplicationContext(), "Pas de tache", Toast.LENGTH_SHORT)
                        .show();
                Intent result = new Intent();
                setResult(Activity.RESULT_CANCELED, result);
                this.finish();
            }

            // Récupérer la date (due to)
            try {
                DateFormat formater = new SimpleDateFormat("MMMM d, yyyy", Locale.FRENCH);
                d = formater.parse(i.getStringExtra("TODO_DUETO"));
            } catch (ParseException e) {
                Toast.makeText(getApplicationContext(), "Pb conversion de date", Toast.LENGTH_SHORT)
                        .show();
                Intent result = new Intent();
                setResult(Activity.RESULT_CANCELED, result);
                this.finish();
            }

            // Autres infos
            String comm = i.getStringExtra("TODO_COMMENT");
            String todo = i.getStringExtra("TODO_TODO");
            String title = i.getStringExtra("TODO_TITLE");
            String ww = i.getStringExtra("TODO_WHITHWHO");

            // Positionnement dans les composants du layout
            TextView tv ;

            tv = (TextView) findViewById(R.id.aff_tv_note_id);
            tv.setText(todo);

            tv = (TextView) findViewById(R.id.aff_tv_correspondant_id);
            tv.setText(ww);

            tv = (TextView) findViewById(R.id.aff_tv_commentaire_id);
            tv.setText(comm);

            Calendar cal = Calendar.getInstance();
            cal.setTime(d);

            DatePicker dp = (DatePicker)findViewById(R.id.aff_dp_pour_id);
            dp.init(cal.get(Calendar.YEAR),
                    cal.get(Calendar.MONTH),
                    cal.get(Calendar.DAY_OF_MONTH),
                    null);
            dp.setEnabled(false);

            tv = (TextView) findViewById(R.id.aff_tv_titre_id);
            tv.setText(title);
            tv.setEnabled(true);

            Button bok = (Button) findViewById(R.id.aff_but_annuler_id);
            bok.setOnClickListener(this);
        }

        @Override
        public void onClick(View v) {
            // A la fin : Réponse de fin ok
            Intent result = new Intent();
            result.putExtra("RES", "Une valeur de retour pour tester ...");
            setResult(Activity.RESULT_OK, result);
            this.finish();
        }
}
