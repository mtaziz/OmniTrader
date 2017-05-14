var my_store = Ext.create("Ext.data.Store", {
    model: "Stock",
    proxy: {
        type: "ajax",
        url: root_url + "/stocks/tags/",
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
Ext.define('OmniTrader.view.TagSearchView', {
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
                                my_store.load({params: {tags: Ext.getCmp('tf_tags').getValue()}})
                            }
                        }
                    }
                ]
            }, {
                xtype: 'list',
                id: 'list_stocks',
                store: my_store,
                itemTpl: '{ticker} {name}',
                listeners: {
                    'itemtap': function (list,  index, target, record, e, eOpts) {
                        Ext.Msg.alert(record.data.ticker)
                    }
                },
                flex: 1
            }
        ]

    }
});