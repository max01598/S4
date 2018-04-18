package com.cdam.tp3;

import android.app.Activity;
import android.content.DialogInterface;
import java.text.DateFormat;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.ContextMenu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;
import android.app.AlertDialog;
import com.cdam.tp3.model.Todo;
import com.cdam.tp3.model.TodoListData;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;
import java.util.Locale;
import java.util.zip.Inflater;

public class MainActivity extends AppCompatActivity
        implements AdapterView.OnItemLongClickListener
{

    private TodoListAdapter tlAdapter;
    private Date d;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tlAdapter = new TodoListAdapter(this, new TodoListData());

        ListView lv = (ListView) findViewById(R.id.mylistView);

        lv.setAdapter(tlAdapter);


        lv.setOnItemLongClickListener(this);
        lv.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {

                Todo td = (Todo)MainActivity.this.tlAdapter.getItem(position);
                String s = "clic sur " + position + " id " + id + " titre " + td.getTitle();
                Toast t = Toast.makeText(getApplicationContext(), s, Toast.LENGTH_SHORT) ;
                t.show();
            }
        });
        this.registerForContextMenu(lv);

    }

    @Override
    public boolean onItemLongClick(AdapterView<?> parent, View view, int position, long id) {
        Todo td = (Todo)this.tlAdapter.getItem(position);
        String s = "clic long sur " + position + " id " + id + " titre " + td.getTitle();
        Toast t = Toast.makeText(getApplicationContext(), s, Toast.LENGTH_SHORT) ;
        t.show();
        return false;
    }

    @Override
    public void onCreateContextMenu(ContextMenu menu, View v, ContextMenu.ContextMenuInfo menuInfo) {
        super.onCreateContextMenu(menu, v, menuInfo);
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.list_todo_menu, menu);
        menu.setHeaderTitle("Choisir");
    }

    @Override
    public boolean onContextItemSelected(MenuItem item) {
        Toast t;
        AdapterView.AdapterContextMenuInfo
                info = (AdapterView.AdapterContextMenuInfo) item.getMenuInfo();
        int pos = info.position; // rang de la ligne sélectionnée dans la listview.
        final int id = (int)info.id ; // id de l’élément todo sélectionné dans la listview.

        if(item.getItemId()==R.id.listview_menu_delete_todo_id){
            AlertDialog.Builder aDBuilder = new AlertDialog.Builder(this);
            aDBuilder.setTitle("Supprimer ?");
            aDBuilder.setMessage("Voulez vous vraiment supprimer ?");
            aDBuilder.setPositiveButton("Oui",
                    new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialog, int which) {
                            tlAdapter.removeById(id);
                            dialog.dismiss();
                        }
                    });
            aDBuilder.setNegativeButton("Non",
                    new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialog, int which) {
                            dialog.dismiss();
                        }
                    });
            AlertDialog alert = aDBuilder.create();
            alert.show();
            t = Toast.makeText(getApplicationContext(), "delete click" + pos, Toast.LENGTH_SHORT);
            t.show();
        }else if(item.getItemId()==R.id.listview_menu_modify_todo_id) {
            t = Toast.makeText(getApplicationContext(), "modify click" + pos, Toast.LENGTH_SHORT);
            t.show();
        }else if (item.getItemId()==R.id.listview_menu_show_todo_id){
            Intent intent;
            intent = new Intent(this, AfficheurTodo.class);
            Todo td = tlAdapter.getItem(id);
            DateFormat formater = new SimpleDateFormat("MMMM d, yyyy", Locale.FRENCH);
            String s = formater.format(td.getDueTo());


            intent.putExtra("TODO_ID",td.getId());
            intent.putExtra("TODO_DUETO", s);
            intent.putExtra("TODO_COMMENT", td.getComment());
            intent.putExtra("TODO_TODO", td.getTodo());
            intent.putExtra("TODO_TITLE", td.getTitle());
            intent.putExtra("TODO_WHITHWHO", td.getWhithWho());
            startActivityForResult(intent, 100);
            t = Toast.makeText(getApplicationContext(), "show click" + pos, Toast.LENGTH_SHORT);
            t.show();
        }
        return super.onContextItemSelected(item);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == 100){
            Toast t;
            if(resultCode ==  Activity.RESULT_CANCELED ){
                t = Toast.makeText(getApplicationContext(), "Cancel", Toast.LENGTH_SHORT);
                t.show();
            }else if (resultCode ==  Activity.RESULT_OK){
                String s = data.getStringExtra("RES");
                t = Toast.makeText(getApplicationContext(), "OK"+s, Toast.LENGTH_SHORT);
                t.show();
            }
        }else if(requestCode == 200 ){
            Toast t;
            if (resultCode ==  Activity.RESULT_OK){
                Intent i;
                i = this.getIntent();
                int taskid = i.getIntExtra("TODO_ID", -1);
                if (taskid == -1) {
                    // Si pas de Todo : Réponse de fin cancel
                    Toast.makeText(getApplicationContext(), "Pas de tache", Toast.LENGTH_SHORT)
                            .show();
                    Intent result = new Intent();
                    setResult(Activity.RESULT_CANCELED, result);
                    this.finish();
                }
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

                String comm = i.getStringExtra("TODO_COMMENT");
                String todo = i.getStringExtra("TODO_TODO");
                String title = i.getStringExtra("TODO_TITLE");
                String ww = i.getStringExtra("TODO_WHITHWHO");
                Todo td ;
                td = new Todo(title,todo,ww,comm,d);
                tlAdapter.add(td);

                String s = data.getStringExtra("RES");
                t = Toast.makeText(getApplicationContext(), "OK"+s, Toast.LENGTH_SHORT);
                t.show();
            }
        }
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();
        Intent intent;
        intent = new Intent(this, EditeurTodo.class);
        startActivityForResult(intent, 200);
        if(id == R.id.main_menu_ajouter_todo_id){
            Toast t;
            t = Toast.makeText(getApplicationContext(), "OptionItemSelected", Toast.LENGTH_SHORT);
            t.show();
        }

        return true;
    }


}
