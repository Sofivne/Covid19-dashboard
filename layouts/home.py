from dash import html

home = html.Div(
    [
        html.H1("COVID-19 : Explorer les Données Mondiales", className="home-text"),
        html.H3("Bienvenue sur notre Dashboard d'Exploration de Données Publiques !"),
        html.Div([
                            html.P("Ce tableau de bord interactif a été conçu pour vous offrir une expérience immersive dans "
                                "l'univers des données publiques, illustrant de manière visuelle et informative un sujet "
                                "d'intérêt public que nous avons choisi avec soin."),
                            html.P(
                                "Notre choix s'est porté sur un sujet pertinent pour lequel nous avons exploré et sélectionné "
                                "des données volumineuses, nous permettant de générer des visualisations détaillées et "
                                "instructives. À travers ce tableau de bord, vous découvrirez un histogramme et une "
                                "représentation géolocalisée dynamique, reflétant notre analyse approfondie du sujet choisi."),
                            html.P(
                                "Nous avons à cœur de vous offrir une expérience interactive et informative, où la richesse "
                                "des données sélectionnées se conjugue à la facilité d'utilisation de notre interface. Nous "
                                "vous invitons à explorer et interagir avec les graphiques pour découvrir des informations "
                                "précieuses sur le sujet que nous avons étudié."),
                            html.P(
                                "Nous vous remercions de vous joindre à nous dans cette exploration de données ouvertes et "
                                "espérons que cette expérience vous sera aussi instructive et intéressante que passionnante !")
                        ])
    ],
    className="home"
)
