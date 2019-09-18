<?php
namespace frontend\controllers;

use yii\web\Controller;

class TestController extends Controller
{
    public function actionIndex() {
        echo 'test';
        $data = 'Hello....';
        return $this->render('index',['data' => $data ]);
    }
    public function actionTest() {
        echo 'Test';
        return $this->render('Test');
    }
}