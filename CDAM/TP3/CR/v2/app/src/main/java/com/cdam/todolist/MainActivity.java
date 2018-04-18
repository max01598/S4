package com.cdam.todolist;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import com.cdam.todolist.model.Todo;
import com.cdam.todolist.model.TodoListAdapter;
import com.cdam.todolist.model.TodoListData;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        TodoListAdapter adapter = new TodoListAdapter(this, new TodoListData());
        ListView listV = findViewById(R.id.liste);
        listV.setAdapter(adapter);

    }
}
