# MOTUS BY VDE — Guide Complet (de zéro à en ligne)

---

## ÉTAPE 0 : CE QUE TU AS DÉJÀ

Tu as téléchargé depuis Claude :
- **motus-vde.html** — le jeu complet
- **generer_mots.py** — le script qui crée les listes de mots

Tu n'as rien d'autre besoin de télécharger depuis Claude.

---

## ÉTAPE 1 : INSTALLE PYTHON (5 min)

Python est un logiciel gratuit qui permet de lancer le script `generer_mots.py`.

### Sur Windows

1. Va sur **https://www.python.org/downloads/**
2. Clique le gros bouton jaune **« Download Python 3.x.x »**
3. Lance le fichier `.exe` téléchargé
4. **⚠️ TRÈS IMPORTANT** : en bas de la fenêtre d'installation, **coche la case "Add Python to PATH"**
5. Clique **« Install Now »**
6. Attends que ça finisse, ferme

### Sur Mac

1. Va sur **https://www.python.org/downloads/**
2. Clique **« Download Python 3.x.x »**
3. Ouvre le fichier `.pkg` téléchargé
4. Clique « Continuer » à chaque étape, puis « Installer »

### Vérifier que ça marche

Ouvre un **terminal** :
- **Windows** : tape `cmd` dans la barre de recherche Windows, clique sur « Invite de commandes »
- **Mac** : ouvre l'app « Terminal » (dans Applications > Utilitaires)

Tape :
```
python3 --version
```
(sur Windows, essaie `python --version` si `python3` ne marche pas)

Tu dois voir quelque chose comme `Python 3.12.x`. Si oui, c'est bon.

---

## ÉTAPE 2 : CRÉE TON DOSSIER DE TRAVAIL (1 min)

Crée un dossier quelque part sur ton PC. Par exemple :

- **Windows** : `C:\Users\TonNom\Documents\motus-vde\`
- **Mac** : `/Users/TonNom/Documents/motus-vde/`

Mets dedans les 2 fichiers téléchargés depuis Claude :
```
motus-vde/
  ├── motus-vde.html
  └── generer_mots.py
```

---

## ÉTAPE 3 : TÉLÉCHARGE LA LISTE DE MOTS FRANÇAIS (1 min)

C'est un simple fichier texte avec 336 000 mots français.

1. Ouvre ton navigateur
2. Va sur : **https://www.pallier.org/extra/liste.de.mots.francais.frgut.txt**
3. La page affiche plein de mots. Fais **Ctrl+S** (ou Cmd+S sur Mac)
4. Enregistre le fichier dans ton dossier `motus-vde/`
5. Le fichier s'appelle `liste.de.mots.francais.frgut.txt`

Ton dossier ressemble maintenant à :
```
motus-vde/
  ├── motus-vde.html
  ├── generer_mots.py
  └── liste.de.mots.francais.frgut.txt
```

---

## ÉTAPE 4 : LANCE LE SCRIPT PYTHON (2 min)

Le script va lire les 336 000 mots, garder seulement ceux de 5 à 9 lettres,
et créer les 2 fichiers JavaScript dont le jeu a besoin.

### Ouvre le terminal dans ton dossier

**Windows :**
1. Ouvre l'Explorateur de fichiers
2. Va dans ton dossier `motus-vde`
3. Clique dans la barre d'adresse en haut (là où il y a le chemin du dossier)
4. Tape `cmd` et appuie Entrée → un terminal s'ouvre directement dans le bon dossier

**Mac :**
1. Ouvre le Terminal
2. Tape `cd ` (avec un espace après), puis glisse ton dossier `motus-vde` dans le terminal
3. Appuie Entrée

### Lance le script

Tape cette commande et appuie Entrée :

```
python3 generer_mots.py liste.de.mots.francais.frgut.txt
```

(Sur Windows, remplace `python3` par `python` si ça ne marche pas)

### Ce que tu dois voir

```
📖 Chargement de liste.de.mots.francais.frgut.txt...

📊 Statistiques :
   5 lettres : 856 solutions / 4521 proposables
   6 lettres : 1203 solutions / 7842 proposables
   7 lettres : 1547 solutions / 12053 proposables
   8 lettres : 1122 solutions / 15234 proposables
   9 lettres : 894 solutions / 11432 proposables
   TOTAL : 5622 solutions / 51082 proposables

✅ Fichiers générés :
   motsSolutions.js (48 Ko)
   motsProposables.js (412 Ko)
```

(Les chiffres exacts varieront un peu)

Ton dossier contient maintenant :
```
motus-vde/
  ├── motus-vde.html
  ├── generer_mots.py
  ├── liste.de.mots.francais.frgut.txt
  ├── motsSolutions.js          ← NOUVEAU
  └── motsProposables.js        ← NOUVEAU
```

---

## ÉTAPE 5 : CONNECTE LES FICHIERS ENSEMBLE (3 min)

Ouvre `motus-vde.html` avec un **éditeur de texte** :
- **Windows** : clic droit > Ouvrir avec > Bloc-notes (ou mieux : télécharge Notepad++ gratuit sur notepad-plus-plus.org)
- **Mac** : clic droit > Ouvrir avec > TextEdit (passe en mode texte brut : Format > Convertir en texte brut)

### Modification 1 : Décommente les scripts

Cherche ces lignes (vers le haut du fichier, lignes 11-12) :

```html
<!-- <script src="motsSolutions.js"></script> -->
<!-- <script src="motsProposables.js"></script> -->
```

Remplace-les par (tu enlèves les `<!--` et `-->`) :

```html
<script src="motsSolutions.js"></script>
<script src="motsProposables.js"></script>
```

### Modification 2 : Utilise les nouvelles listes

Cherche cette ligne (dans le gros bloc `<script>`) :

```js
const WL = [
```

C'est le début d'une GROSSE liste de mots entre crochets qui finit par `];`.
**Supprime TOUT depuis `const WL = [` jusqu'au `];` inclus** (c'est environ 100 lignes).

À la place, mets juste :

```js
const WL = SOLUTIONS;
```

### Modification 3 : Supprime les extras devenus inutiles

Cherche la ligne :

```js
const _extraProposables = [
```

**Supprime TOUT depuis `const _extraProposables = [` jusqu'au `];` inclus** (encore plein de lignes de mots).

Puis cherche la ligne qui commence par :

```js
const PROPOSABLES = (typeof window.PROPOSABLES
```

Et remplace cette ligne (et la suivante avec le `:`) par :

```js
// PROPOSABLES est défini dans motsProposables.js, rien à faire ici
```

### Modification 4 : Renomme le fichier

Renomme `motus-vde.html` en **`index.html`**

Ton dossier final :
```
motus-vde/
  ├── index.html              ← le jeu (renommé)
  ├── motsSolutions.js        ← ~5000 mots à deviner
  ├── motsProposables.js      ← ~50000 mots acceptés
  ├── generer_mots.py         ← tu peux le garder au cas où
  └── liste.de.mots.francais.frgut.txt  ← tu peux supprimer
```

---

## ÉTAPE 6 : TESTE EN LOCAL (30 sec)

Double-clique sur `index.html` → ça s'ouvre dans ton navigateur.

**⚠️ Ça ne marchera peut-être pas directement** parce que les navigateurs
bloquent le chargement de fichiers `.js` locaux pour des raisons de sécurité.

Si le jeu s'affiche mais les mots ne marchent pas, fais plutôt :

### Méthode simple : mini serveur local

Ouvre un terminal dans ton dossier `motus-vde` et tape :

```
python3 -m http.server 8080
```

Puis ouvre ton navigateur et va sur :

```
http://localhost:8080
```

Le jeu s'ouvre. Teste tous les modes. Quand tu as fini, reviens dans le terminal et fais Ctrl+C pour arrêter.

---

## ÉTAPE 7 : METS EN LIGNE SUR NETLIFY (2 min, GRATUIT)

1. Va sur **https://app.netlify.com/drop**
   (Pas besoin de compte pour le premier déploiement)

2. Tu vois une zone qui dit **« Drag and drop your site output folder here »**

3. **Glisse ton dossier `motus-vde/` entier** dans cette zone
   (le dossier, pas les fichiers un par un)

4. Attends 10 secondes

5. **C'est en ligne !** Tu reçois une URL comme :
   `https://gleaming-sunshine-a1b2c3.netlify.app`

6. Pour personnaliser l'URL :
   - Crée un compte Netlify (gratuit)
   - Va dans **Site settings > Domain management > Custom domain**
   - Change le nom en ce que tu veux, ex : `motus-vde.netlify.app`

---

## ÉTAPE 8 : POUR ALLER PLUS LOIN (optionnel)

### Sauvegarder les comptes entre les PC → Supabase

Actuellement les comptes sont dans le navigateur (localStorage).
Pour que les joueurs se connectent depuis n'importe quel PC :

1. Crée un compte sur **https://supabase.com** (gratuit)
2. Crée un projet
3. Dans le SQL Editor, crée les tables (accounts, history, etc.)
4. Récupère l'URL et la clé API dans Settings > API
5. Ajoute le SDK Supabase dans le HTML et remplace les appels localStorage

### Multi en temps réel → Supabase Realtime

Même Supabase, tu actives « Realtime » sur tes tables et les joueurs
se voient en direct via WebSocket (pas de polling).

### Nom de domaine personnalisé → ~10€/an

Achète un domaine sur OVH, Namecheap, ou Gandi, puis connecte-le à Netlify.

---

## RÉCAP DES COÛTS

| Quoi | Combien |
|------|---------|
| Python | Gratuit |
| Liste de mots | Gratuit |
| Netlify (hébergement) | Gratuit |
| Supabase (comptes + multi) | Gratuit |
| Nom de domaine | ~10€/an (optionnel) |
| **TOTAL** | **0€** |

---

## EN CAS DE PROBLÈME

**« python3 n'est pas reconnu »**
→ Sur Windows, essaie `python` au lieu de `python3`. Si ça ne marche pas, réinstalle Python en cochant bien "Add to PATH".

**« Le fichier est introuvable »**
→ Vérifie que tu es bien dans le bon dossier dans le terminal. Tape `dir` (Windows) ou `ls` (Mac) pour voir les fichiers.

**« Le jeu s'affiche mais tous les mots sont refusés »**
→ Les fichiers JS ne sont pas chargés. Utilise la méthode `python3 -m http.server 8080` pour tester.

**« Netlify dit erreur »**
→ Vérifie que ton dossier contient bien un fichier nommé exactement `index.html` (pas `motus-vde.html`).
