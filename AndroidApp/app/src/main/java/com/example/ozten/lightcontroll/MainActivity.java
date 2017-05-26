package com.example.ozten.lightcontroll;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.widget.RelativeLayout;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);



        WebView webView = (WebView) findViewById(R.id.webview);
        WebSettings settings = webView.getSettings();
        //webView.setInitialScale(1);
        settings.setJavaScriptEnabled(true);
        settings.setLoadWithOverviewMode(true);
        settings.setUseWideViewPort(true);


        webView.setVerticalScrollBarEnabled(false);
        webView.setScrollContainer(false);
        webView.loadUrl("http://192.168.1.4");

    }
}
