var my_store = Ext.create("Ext.data.Store", {
    model: "Stock",
    proxy: {
        type: "ajax",
        url: root_url+"/stocks/tags/",
        extraParams: {
            format: 'json'
        },
        reader: {
            type: "json"
        }
    },
    autoLoad: false
});

var thestore = Ext.create('Ext.data.Store', {
    model: "Stock",
    autoLoad: true,
    data: [{id: 1, name: 'zxzq', ticker: '600030'}]
});
Ext.define('OmniTrader.view.MainView', {
    extend: 'Ext.Panel',
    config: {
        layout: 'hbox',
        items: [
            {
                xtype: 'toolbar',
                docked: 'top',
                items: [
                    {
                        xtype: 'textfield',
                        id: 'tf_tags',
                        docked: 'top',
                        placeHolder: 'Enter tags',
                        enableKeyEvents: true,
                        listeners: {
                            'action': function (field, event, options) {
                                //my_store.getProxy().extraParams.tags = '雄安，环保';
                                my_store.load({params:{tags:Ext.getCmp('tf_tags').getValue()}})
                            }
                        }
                    }
                ]
            }, {
                xtype: 'list',
                store: my_store,
                itemTpl: '{ticker} {name}',
                flex: 1
            }
        ]

    }
});


Ext.application({
    name: 'Sencha',

    launch: function () {
        var panel = Ext.create('OmniTrader.view.MainView')
        Ext.Viewport.add(panel);
    }
});