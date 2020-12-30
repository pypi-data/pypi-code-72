from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats_female = (
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}-{{last_name}}',
        '{{first_name_female}}-{{first_name_female}} {{last_name}}',
    )

    formats_male = (
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}-{{last_name}}',
        '{{first_name_male}}-{{first_name_male}} {{last_name}}',
    )

    formats = formats_male + formats_female

    # Source:
    # https://www.retraitequebec.gouv.qc.ca/fr/services-en-ligne-outils/banque-de-prenoms/Pages/banque-de-prenoms.aspx
    first_names_male = (
        'Alain',
        'Alexandre',
        'Alexis',
        'André',
        'Antoine',
        'Arthur',
        'Benjamin',
        'Benoît',
        'Bernard',
        'Bertrand',
        'Charles',
        'Daniel',
        'David',
        'Denis',
        'Édouard',
        'Émile',
        'Emmanuel',
        'Éric',
        'Étienne',
        'François',
        'Frédéric',
        'Gabriel',
        'Georges',
        'Gérard',
        'Gilbert',
        'Gilles',
        'Grégoire',
        'Guillaume',
        'Guy',
        'William',
        'Henri',
        'Hugues',
        'Jacques',
        'Jean',
        'Jérôme',
        'Jonathan',
        'Joseph',
        'Jules',
        'Julien',
        'Kevin',
        'Laurent',
        'Louis',
        'Luc',
        'Lucas',
        'Marc',
        'Maxime',
        'Marcel',
        'Martin',
        'Mathieu',
        'Maurice',
        'Michel',
        'Nathan',
        'Nicolas',
        'Noël',
        'Olivier',
        'Patrick',
        'Paul',
        'Philippe',
        'Pierre',
        'Raphaël',
        'Raymond',
        'Rémy',
        'René',
        'Richard',
        'Robert',
        'Roger',
        'Roland',
        'Samuel',
        'Sébastien',
        'Stéphane',
        'Théodore',
        'Thomas',
        'Timothée',
        'Tristan',
        'Victor',
        'Vincent',
        'Xavier',
        'Yves',
        'Zacharie',
    )

    first_names_female = (
        'Agnès',
        'Alexandra',
        'Alex',
        'Alice',
        'Amélie',
        'Anaïs',
        'Andrée',
        'Anne',
        'Anouk',
        'Astrid',
        'Audrey',
        'Aurélie',
        'Aurore',
        'Béatrice',
        'Brigitte',
        'Camille',
        'Caroline',
        'Catherine',
        'Cécile',
        'Céline',
        'Célina',
        'Chantal',
        'Charlotte',
        'Christelle',
        'Christiane',
        'Christine',
        'Claire',
        'Claudine',
        'Claude',
        'Clémence',
        'Colette',
        'Constance',
        'Danielle',
        'Denise',
        'Diane',
        'Dominique',
        'Dorothée',
        'Édith',
        'Emma',
        'Éléonore',
        'Élisabeth',
        'Élise',
        'Élodie',
        'Émilie',
        'Emmanuelle',
        'Florence',
        'Françoise',
        'Frédérique',
        'Gabrielle',
        'Geneviève',
        'Hélène',
        'Henriette',
        'Hortense',
        'Isabelle',
        'Jacqueline',
        'Jeanne',
        'Jeannine',
        'Jessica',
        'Joséphine',
        'Josette',
        'Julie',
        'Juliette',
        'Karine',
        'Laetitia',
        'Laurence',
        'Laurie',
        'Lorraine',
        'Louise',
        'Lucie',
        'Lucy',
        'Manon',
        'Marcelle',
        'Marguerite',
        'Margot',
        'Margaret',
        'Marianne',
        'Marie',
        'Martine',
        'Maryse',
        'Maude',
        'Mathilde',
        'Mélanie',
        'Michèle',
        'Michelle',
        'Monique',
        'Nathalie',
        'Nathalie',
        'Nicole',
        'Noémie',
        'Océane',
        'Odette',
        'Olivia',
        'Patricia',
        'Paulette',
        'Pauline',
        'Pénélope',
        'Renée',
        'Rosalie',
        'Sarah',
        'Simone',
        'Sophie',
        'Stéphanie',
        'Susanne',
        'Sylvie',
        'Thérèse',
        'Vanessa',
        'Valérie',
        'Véronique',
        'Virginie',
        'Zoé',
    )

    first_names = first_names_male + first_names_female

    # Source:
    # https://fr.wikipedia.org/wiki/Liste_des_noms_de_famille_les_plus_courants_au_Qu%C3%A9bec
    last_names = (
        'Tremblay',
        'Gagnon',
        'Roy',
        'Côté',
        'Bouchard',
        'Gauthier',
        'Morin',
        'Lavoie',
        'Fortin',
        'Gagné',
        'Ouellet',
        'Pelletier',
        'Bélanger',
        'Lévesque',
        'Bergeron',
        'Leblanc',
        'Paquette',
        'Girard',
        'Simard',
        'Boucher',
        'Caron',
        'Beaulieu',
        'Cloutier',
        'Dubé',
        'Poirier',
        'Fournier',
        'Lapointe',
        'Leclerc',
        'Lefebvre',
        'Poulin',
        'Thibault',
        'St-Pierre',
        'Nadeau',
        'Martin',
        'Landry',
        'Martel',
        'Bédard',
        'Grenier',
        'Lessard',
        'Bernier',
        'Richard',
        'Michaud',
        'Hébert',
        'Desjardins',
        'Couture',
        'Turcotte',
        'Lachance',
        'Parent',
        'Blais',
        'Gosselin',
        'Savard',
        'Proulx',
        'Beaudoin',
        'Demers',
        'Perreault',
        'Boudreau',
        'Lemieux',
        'Cyr',
        'Perron',
        'Dufour',
        'Dion',
        'Mercier',
        'Bolduc',
        'Bérubé',
        'Boisvert',
        'Langlois',
        'Ménard',
        'Therrien',
        'Plante',
        'Bilodeau',
        'Blanchette',
        'Dubois',
        'Champagne',
        'Paradis',
        'Fortier',
        'Arsenault',
        'Dupuis',
        'Gaudreault',
        'Hamel',
        'Houle',
        'Villeneuve',
        'Rousseau',
        'Gravel',
        'Thériault',
        'Lemay',
        'Robert',
        'Allard',
        'Deschênes',
        'Giroux',
        'Guay',
        'Leduc',
        'Boivin',
        'Charbonneau',
        'Lambert',
        'Raymond',
        'Vachon',
        'Gilbert',
        'Audet',
        'Jean',
        'Larouche',
        'Legault',
        'Trudel',
        'Fontaine',
        'Picard',
        'Labelle',
        'Lacroix',
        'Jacques',
        'Moreau',
        'Carrier',
        'Bernard',
        'Desrosiers',
        'Goulet',
        'Renaud',
        'Dionne',
        'Lapierre',
        'Vaillancourt',
        'Fillion',
        'Lalonde',
        'Tessier',
        'Bertrand',
        'Tardif',
        'Lepage',
        'Gingras',
        'Benoît',
        'Rioux',
        'Giguère',
        'Drouin',
        'Harvey',
        'Lauzon',
        'Nguyen',
        'Gendron',
        'Boutin',
        'Laflamme',
        'Vallée',
        'Dumont',
        'Breton',
        'Paré',
        'Paquin',
        'Robitaille',
        'Gélinas',
        'Duchesne',
        'Lussier',
        'Séguin',
        'Veilleux',
        'Potvin',
        'Gervais',
        'Pépin',
        'Laroche',
        'Morissette',
        'Charron',
        'Lavallée',
        'Laplante',
        'Chabot',
        'Brunet',
        'Vézina',
        'Desrochers',
        'Labrecque',
        'Coulombe',
        'Tanguay',
        'Chouinard',
        'Noël',
        'Pouliot',
        'Lacasse',
        'Daigle',
        'Marcoux',
        'Lamontagne',
        'Turgeon',
        'Larocque',
        'Roberge',
        'Auger',
        'Massé',
        'Pilon',
        'Racine',
        'Dallaire',
        'Émond',
        'Grégoire',
        'Beauregard',
        'Smith',
        'Denis',
        'Lebel',
        'Blouin',
        'Martineau',
        'Labbé',
        'Beauchamp',
        'St-Onge',
        'Charette',
        'Dupont',
        'Létourneau',
        'Rodrigue',
        'Cormier',
        'Rivard',
        'Mathieu',
        'Asselin',
        'St-Jean',
        'Plourde',
        'Thibodeau',
        'Bélisle',
        'St-Laurent',
        'Godin',
        'Desbiens',
        'Lavigne',
        'Doucet',
        'Labonté',
        'Marchand',
        'Brassard',
        'Forget',
        'Patel',
        'Marcotte',
        'Béland',
        'Larose',
        'Duval',
        'Archambault',
        'Maltais',
        'Trépanier',
        'Laliberté',
        'Bisson',
        'Brisson',
        'Dufresne',
        'Beaudry',
        'Chartrand',
        'Houde',
        'Fréchette',
        'Lafontaine',
        'Guillemette',
        'Drolet',
        'Vincent',
        'Richer',
        'Germain',
        'Larivière',
        'Ferland',
        'Trottier',
        'Piché',
        'Boulanger',
        'Sirois',
        'Charest',
        'Provost',
        'Durand',
        'Dumas',
        'Soucy',
        'Lamoureux',
        'Lachapelle',
        'Bégin',
        'Boily',
        'Croteau',
        'Savoie',
        'Provencher',
        'Prévost',
        'Duguay',
        'Lemire',
        'Delisle',
    )
