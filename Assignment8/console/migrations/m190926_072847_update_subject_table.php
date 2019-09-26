<?php

use yii\db\Migration;

/**
 * Class m190926_072847_update_subject_table
 */
class m190926_072847_update_subject_table extends Migration
{
    /**
     * {@inheritdoc}
     */
    public function safeUp()
    {
        $this->addColumn('Subject','create_at',$this->integer());
        $this->addColumn('Subject','create_by',$this->integer());
        $this->addColumn('Subject','update_at',$this->integer());
        $this->addColumn('Subject','update_by',$this->integer());
    }

    /**
     * {@inheritdoc}
     */
    public function safeDown()
    {
        echo "m190926_072847_update_subject_table cannot be reverted.\n";

        return false;
    }

    /*
    // Use up()/down() to run migration code without a transaction.
    public function up()
    {

    }

    public function down()
    {
        echo "m190926_072847_update_subject_table cannot be reverted.\n";

        return false;
    }
    */
}
