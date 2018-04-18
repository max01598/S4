package com.cdam.tp3;

/**
 * Created by André Péninou on 09/02/2018.
 */

import android.widget.BaseAdapter;

import android.content.Context;
import android.graphics.Color;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.LinearLayout;
import android.widget.TextView;

import java.text.SimpleDateFormat;

import com.cdam.tp3.model.Todo;
import com.cdam.tp3.model.TodoListData;


public class TodoListAdapter extends BaseAdapter {

    private TodoListData tlData;

    private Context context;
    private LayoutInflater li;

    private SimpleDateFormat sdf = new SimpleDateFormat("dd-MM-yyyy");

    public TodoListAdapter(Context _context, TodoListData _tlD) {
        this.context = _context;
        this.tlData = _tlD;
        this.li = LayoutInflater.from(context);
    }
    @Override
    public int getCount() {
        return this.tlData.size();
    }

    @Override
    public Todo getItem(int position) {
        return this.tlData.get(position);
    }

    @Override
    public long getItemId(int position) {
        return this.tlData.get(position).getId();
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        LinearLayout layoutItem;
        String s;

        // (1) : Reutilisation des layouts
        if (convertView == null) {
            // Initialisation de notre item a partir du layout XML
            // "todoviewer.xml"
            layoutItem = (LinearLayout) this.li.inflate(R.layout.todoviewer, null);
        } else {
            layoutItem = (LinearLayout) convertView;
        }

        // (3) : Recuperation des TextView de notre layout
        TextView tv_titre = (TextView) layoutItem
                .findViewById(R.id.tv_todoviewer_titre_id);
        TextView tv_todo = (TextView) layoutItem
                .findViewById(R.id.tv_todoviewer_todo_id);
        TextView tv_wwc = (TextView) layoutItem
                .findViewById(R.id.tv_todoviewer_wwcomment_id);
        TextView tv_date = (TextView) layoutItem
                .findViewById(R.id.tv_todoviewer_date_id);

        // (4) Récupérer le Todo à afficher

        Todo td = this.tlData.get(position);

        // (5) : Renseignement des valeurs

        tv_titre.setText("" + td.getId() + " "
                + td.getTitle());
        s = td.getTodo();
        if (s.length() > 40) {
            s = s.substring(0, 39);
        }
        tv_todo.setText(s);

        s = "(" + td.getWhithWho() + ")"
                + "(" + td.getComment() + ")";
        if (s.length() > 40) {
            s = s.substring(0, 39);
        }
        tv_wwc.setText(s);

        tv_date.setText(this.sdf.format(td.getDueTo()));

        // Changement de la couleur du fond des items
        if (position % 2 == 0) {
            tv_titre.setTextColor(Color.BLACK);
            tv_todo.setTextColor(Color.BLACK);
            tv_wwc.setTextColor(Color.BLACK);
            tv_date.setTextColor(Color.BLACK);
        } else {
            tv_titre.setTextColor(Color.LTGRAY);
            tv_todo.setTextColor(Color.LTGRAY);
            tv_wwc.setTextColor(Color.LTGRAY);
            tv_date.setTextColor(Color.LTGRAY);
        }

        // On retourne l'item cree.
        return layoutItem;
    }

    public void removeById(int id){
        this.tlData.removeById(id);
        this.notifyDataSetChanged();
    }

    public void add(Todo tdNew){
        this.tlData.add(tdNew);
        this.notifyDataSetChanged();
    }

}
