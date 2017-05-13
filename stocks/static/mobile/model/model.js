Ext.define('Stock', {
    extend: 'Ext.data.Model',

    config: {
        fields: ['id', 'ticker', 'name']
        //hasMany: 'Tag'
    }
});

Ext.define('Tag', {
    extend: 'Ext.data.Model',

    config: {
        fields: ['id', 'stock_id', 'name', 'slug'],
        belongsTo: 'User'
    }
});