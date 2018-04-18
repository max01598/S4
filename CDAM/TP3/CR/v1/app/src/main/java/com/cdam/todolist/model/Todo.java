package com.cdam.todolist.model;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class Todo {

    private static int lastId = 1000;

    private int id;
    private String title, todo, whithWho, comment;
    private Date dueTo;

    public Todo(String title, String todo) {
        super();
        this.id = Todo.lastId+1;
        Todo.lastId++;
        this.title = title;
        this.todo = todo;
        this.whithWho = "";
        Calendar cal = Calendar.getInstance();
        cal.set(2099,0,1);
        this.dueTo = cal.getTime();
        this.comment = "";
    }

    public Todo(String title, String todo, String whithWho, String comment,
                Date dueTo) {
        super();
        this.id = Todo.lastId+1;
        Todo.lastId++;
        this.title = title;
        this.todo = todo;
        this.whithWho = whithWho;
        this.comment = comment;
        this.dueTo = dueTo;
    }

    public int getId() {
        return this.id;
    }

    public String getTitle() {
        return title;
    }

    public String getTodo() {
        return todo;
    }

    public String getWhithWho() {
        return whithWho;
    }

    public String getComment() {
        return comment;
    }

    public Date getDueTo() {
        return dueTo;
    }

    public String toString () {
        SimpleDateFormat sdf = new SimpleDateFormat("dd-MM-yyyy");
        return ""+this.id
                +" "
                +this.title
                +" : "
                +this.todo
                +" - "
                +sdf.format(this.dueTo)
                +" ("
                +this.whithWho
                +")("
                +this.comment
                +")";
    }
}
