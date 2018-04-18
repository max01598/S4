package com.cdam.todolist;

import android.content.Context;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import com.cdam.todolist.model.Todo;
import com.cdam.todolist.model.TodoListAdapter;
import com.cdam.todolist.model.TodoListData;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity implements AdapterView.OnItemLongClickListener{
    private TodoListAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        TodoListAdapter adapter = new TodoListAdapter(this, new TodoListData());
        ListView listV = findViewById(R.id.liste);
        listV.setAdapter(adapter);


        listV.setOnItemLongClickListener(this);
        listV.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                Todo td = (Todo)MainActivity.this.adapter.getItem(position);
                String s = " click simple / position : " + position + " id :" + id + " titre :" + td.getTitle();
                Toast t = Toast.makeText(getApplicationContext(), s, Toast.LENGTH_SHORT) ;
                t.show();
            }
        });
    }

    public boolean onItemLongClick(AdapterView<?> parent, View view, int position, long id) {
        Todo td = (Todo)this.adapter.getItem(position);
        String s = "clic long / position : " + position + " id : " + id + " titre : " + td.getTitle();
        Toast t = Toast.makeText(getApplicationContext(), s, Toast.LENGTH_SHORT) ;
        t.show();
        return true;
    }
}
