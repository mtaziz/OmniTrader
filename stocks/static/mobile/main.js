tagview = Ext.create('OmniTrader.view.TagSearchView')

Ext.define('OmniTrader.view.MainView', {
    extend: 'Ext.NavigationView',
    alias: ['omnitrader'],
    title: 'OmniTrader',
    config: {
        fullscreen: true,
        items: [],
        listeners: {
            'swipe': function (e, node, options, eOpts) {
                if (e.direction == "right") {

                    this.pop()
                }
            }
        }

    }
})

Ext.application({
    name: 'OmniTrader',

    launch: function () {
        var mainView = Ext.create('omnitrader')
        var panel = Ext.create('ot-tagsearchview')
        panel.title = 'Tag Search';
        Ext.Viewport.add(mainView);
        mainView.push(panel)
    }
});