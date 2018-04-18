package com.cdam.todolist.model;

import android.content.Context;
import android.graphics.Color;
import android.text.Layout;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.cdam.todolist.R;

/**
 * Created by Dark Vador on 19/02/2018.
 */

public class TodoListAdapter extends BaseAdapter {
    private Context context;
    private LayoutInflater layI;
    private TodoListData todoListeD;

    public TodoListAdapter(Context ct, TodoListData tol){
      context= ct;
      layI= LayoutInflater.from(context);
      todoListeD=tol;
    }

    public int getCount(){
        return todoListeD.size();
    }
    public Todo getItem(int position){
        return todoListeD.get(position);
    }
    public long getItemId(int position){
        return todoListeD.get(position).getId();
    }
    public View getView(int position, View convertView, ViewGroup parent){
        LinearLayout l;
        if(convertView==null){
             l = (LinearLayout)layI.inflate(R.layout.todoviewer,null);
        }else{
             l = (LinearLayout)convertView ;
        }
        TextView date = l.findViewById(R.id.tv_todoviewer_date_id);
        TextView titre = l.findViewById(R.id.tv_todoviewer_titre_id);
        TextView todo = l.findViewById(R.id.tv_todoviewer_todo_id);
        TextView comment = l.findViewById(R.id.tv_todoviewer_wwcomment_id);
        Todo tod = this.getItem(position);
        date.setText(tod.getDueTo().toString());
        String donnee = ""+this.getItemId(position)+" "+tod.getTitle();
        titre.setText(donnee);

        if(tod.getTodo().length()>40){
            donnee =tod.getTodo().substring(0,39)+"[...]";
            todo.setText(donnee);
        }else{
            todo.setText(tod.getTodo());
        }



        if(tod.getComment().length()>40){
            donnee =""+tod.getWhithWho()+" "+tod.getComment().substring(0,39)+"[...]";
            comment.setText(donnee);
        }else{
            donnee =""+tod.getWhithWho()+" "+tod.getComment();
            comment.setText(donnee);
        }

        if (position % 2 == 0) {
            titre.setTextColor(Color.BLACK);
            date.setTextColor(Color.BLACK);
            todo.setTextColor(Color.BLACK);
            comment.setTextColor(Color.BLACK);
        } else {
            titre.setTextColor(Color.LTGRAY);
            date.setTextColor(Color.LTGRAY);
            todo.setTextColor(Color.LTGRAY);
            comment.setTextColor(Color.LTGRAY);
        }
        return l;
    }

}
