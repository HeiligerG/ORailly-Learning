# Vue CLI - Erstellung eines Projekts

In diesem Tutorial werden wir unser Projekt mithilfe der Vue CLI erstellen. Wir schauen uns dann die Vue UI an, eine grafische Benutzeroberfläche zur Verwaltung unseres Projekts. Zum Schluss werden wir das vom CLI generierte Projekt erkunden, um uns mit der Arbeit in diesen Dateien und Ordnern vertraut zu machen.

## Warum eine CLI?

Wie du wahrscheinlich weißt, steht CLI für Command Line Interface (Befehlszeilenschnittstelle), und die Vue CLI bietet ein umfassendes System für die schnelle Vue.js-Entwicklung. Das bedeutet, dass sie viele mühsame Arbeiten für uns erledigt und uns wertvolle Funktionen direkt zur Verfügung stellt.

- Sie ermöglicht uns, die Bibliotheken auszuwählen, die unser Projekt verwenden wird
- Dann werden diese automatisch in das Projekt integriert
- Sie konfiguriert Webpack
- Wenn wir unsere App mit Webpack erstellen, werden alle unsere JavaScript-Dateien, unser CSS und unsere Abhängigkeiten ordnungsgemäß gebündelt, minimiert und optimiert
- Sie ermöglicht uns, HTML, CSS und JavaScript nach unseren Vorlieben zu schreiben
- Wir können Single-File .vue-Komponenten, TypeScript, SCSS, Pug, die neuesten Versionen von ECMAScript usw. verwenden
- Sie ermöglicht Hot Module Replacement (HMR)
- Wenn du dein Projekt speicherst, erscheinen Änderungen sofort im Browser

## Installation der CLI

Um die CLI zu verwenden, benötigst du Node.js Version 8.9 oder höher (v10+ empfohlen).

Um die CLI zu installieren, führe diesen Befehl in deinem Terminal aus:

```
npm i -g @vue/cli
# ODER
yarn global add @vue/cli
```

Nach der Installation hast du Zugriff auf die Vue-Binary in deiner Befehlszeile. Wir werden diese verwenden, um unser Projekt zu erstellen.

## Erstellung eines Vue-Projekts

Es gibt zwei Möglichkeiten, unser Projekt zu erstellen: Mit der Vue UI oder direkt über die Befehlszeile, was wir jetzt tun werden, indem wir folgenden Befehl in unserem Terminal ausführen:

```
vue create real-world-vue
```

Dieser Befehl startet die Erstellung eines Vue-Projekts mit dem Namen "real-world-vue".

Wir werden dann aufgefordert, eine Standardvorlage auszuwählen oder Funktionen manuell auszuwählen. Mit der Pfeiltaste nach unten markieren wir "Manually select features" und drücken dann Enter.

Danach wird uns eine Liste mit Funktionsoptionen angezeigt. Mit der Pfeiltaste nach unten bewegen wir uns nach unten und wählen mit der Leertaste Router, Vuex und Linter/Formatter aus. Dann drücken wir Enter.

Als nächstes wählen wir die Version von Vue.js aus, die wir verwenden möchten. Natürlich wählen wir hier Vue 3.

Dann antworten wir mit Y (ja) auf die Frage, ob wir den History-Modus für Vue Router verwenden möchten.

Dann werden wir aufgefordert, einen Linter/Formatter zu wählen, was ganz dir überlassen ist. Ich werde ESLint + Prettier wählen und angeben, dass beim Speichern gelintet werden soll.

Und für diesen Kurs wähle ich dedizierte Konfigurationsdateien, aber wir könnten sie auch in package.json aufbewahren. Auch das bleibt dir überlassen.

Wir haben die Möglichkeit, all diese Einstellungen als Vorlage zu speichern. Ich entscheide mich mit N dagegen.

Wenn du dies als Vorlage speichern möchtest, wird sie in einer JSON-Datei namens .vuerc in deinem Benutzerverzeichnis gespeichert.

Wenn wir Enter drücken, wird unser Projekt automatisch erstellt.

## Ausführen unseres Projekts

Sobald unser Projekt erstellt ist, können wir mit cd hineinwechseln. Um es live in unserem Browser anzuzeigen, führen wir den Befehl `npm run serve` aus, der die App kompiliert und auf einem lokalen Host bereitstellt.

Oben ist unsere App, die live im Browser ausgeführt wird. Sie hat bereits zwei Seiten, die Home-Seite und die About-Seite, zwischen denen wir navigieren können, weil sie Vue Router verwendet.

## Vue UI

Nachdem wir verstanden haben, wie wir ein Vue-Projekt über die Befehlszeile erstellen können, wiederholen wir denselben Prozess mit der Vue UI, die eine intuitive visuelle Möglichkeit zur Verwaltung unserer Vue-Projekte bietet.

Da wir bereits Zugriff auf die Vue-Binary haben, können wir `vue ui` in unser Terminal eingeben, wodurch die Vue UI in unserem Browser gestartet wird.

Um hier ein Projekt zu erstellen, klicken wir auf den Tab "Create", wählen den Ort aus, an dem wir unser Projekt speichern möchten, und klicken dann auf "Create a new project here". Dies führt uns durch alle Projektkonfigurationsschritte, die wir gerade über das Terminal durchgeführt haben.

## Vue UI Funktionen

Vom UI-Dashboard aus können wir Dinge wie Plugin- und Abhängigkeitsupdates für unser Projekt überwachen und Sicherheitsüberprüfungen durchführen.

Du kannst deinem Projekt auch Plugins über die Vue UI hinzufügen, was es sehr einfach macht, eine benötigte Bibliothek wie Vuetify hinzuzufügen.

Wir werden dieses Plugin nicht installieren, aber wenn du mehr über dieses Komponentendesign-Framework erfahren möchtest, gibt es einen kompletten Vuetify-Kurs.

Darüber hinaus können wir alle Abhängigkeiten anzeigen, die unser Projekt verwendet, und neue Abhängigkeiten über die UI hinzufügen. Die UI hat auch einen Tab zur globalen Konfiguration des Projekts, zur Konfiguration von ES-Lint-Regeln und mehr.

Es gibt auch einen Tab zum Ausführen von Aufgaben für unser Projekt.

Wenn wir Aufgaben wie "serve" ausführen, erhalten wir viele hilfreiche visuelle Rückmeldungen über unsere App und wie sie aufgebaut ist und funktioniert.

Wenn du ein Projekt importieren möchtest, das du nicht ursprünglich aus der Vue UI erstellt hast, kannst du dies einfach über den Import-Tab des Projektmanagers tun. Suche einfach dein Projekt und klicke auf "Import this folder".

## Unser Vue-Projekt erkunden

Nachdem wir nun wissen, wie wir unser Projekt über das Terminal und auch über die UI erstellen können, schauen wir uns das für uns erstellte Projekt an.

- Das Verzeichnis **node_modules** enthält alle Bibliotheken, die wir zum Erstellen von Vue benötigen.

- Im Verzeichnis **public** kannst du statische Assets ablegen, die beim Erstellen des Projekts nicht durch Webpack laufen sollen.

- Das Verzeichnis **src** ist der Ort, an dem du die meiste Zeit verbringen wirst, da es den gesamten Anwendungscode enthält.

- Du solltest den Großteil deiner Assets, wie Bilder und Schriftarten, im Verzeichnis **assets** ablegen, damit sie von Webpack optimiert werden können.

- Im Verzeichnis **components** speichern wir die Komponenten oder Bausteine unserer Vue-App.

- Der Ordner **router** wird für Vue Router verwendet, der die Navigation unserer Seite ermöglicht. Wir verwenden Vue Router, um die verschiedenen "Ansichten" unserer Single-Page-Anwendung aufzurufen.

- Der **store** ist der Ort, an dem wir Vuex-Code ablegen, der die Zustandsverwaltung in der App übernimmt. Am Ende dieses Kurses wirst du ein grundlegendes Verständnis dafür haben, wofür Vuex da ist, aber wir werden keinen Vuex-Code implementieren. Dieser Kurs dient als Grundlagenkurs, der dich auf unseren Vuex-Kurs vorbereitet.

- Im Verzeichnis **views** speichern wir Komponentendateien für die verschiedenen Ansichten unserer App, die Vue Router lädt.

- Die Datei **App.vue** ist die Hauptkomponente, in die alle anderen Komponenten eingebettet sind.

- Die Datei **main.js** rendert unsere App.vue-Komponente (und alles, was darin enthalten ist) und bindet sie an das DOM.

- Schließlich haben wir eine Datei **.gitignore**, in der wir festlegen können, was git ignorieren soll, zusammen mit einer Datei **babel.config.js** und unserer **package.json**, die npm bei der Identifizierung des Projekts und der Verwaltung seiner Abhängigkeiten hilft, sowie einer **README.md**.

## Wie die App geladen wird

Du fragst dich jetzt vielleicht, wie die App geladen wird? Schauen wir uns diesen Prozess an.

📁src/main.js

```javascript
import { createAPP } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

createApp(App)
  .use(Router)
  .use(Store)
  .mount("#app");
```

In unserer main.js-Datei importieren wir die createApp-Methode von Vue, zusammen mit unserer App.js-Komponente. Dann führen wir diese Methode aus und übergeben die App (die Hauptkomponente, die den gesamten Anwendungscode enthält, da alle anderen Komponenten darin verschachtelt sind).

Wie der Methodenname ausdrücklich besagt, erstellt dies die App, und wir sagen ihr, dass sie den oben importierten Router und Store verwenden soll. Schließlich wird die App über die mount-Methode an das DOM angehängt, die ein Argument erhält, um anzugeben, wo im DOM die App angehängt werden soll. Aber wo genau ist diese ID "#app"?

Wenn wir in unsere index.html-Datei schauen, sehen wir, dass es ein div mit der ID "app" gibt, mit einem hilfreichen Kommentar darunter.

📁public/index.html

```html
<div id="app"></div>
<!-- built files will be auto-injected -->
```

Ah. Das ist also der Ort, an dem unsere Vue-App angehängt wird. Später werden wir ein tieferes Verständnis dafür bekommen, wie diese index.html als "Single Page" unserer Single-Page-Anwendung dient.

## Alles zusammenfügen

Schauen wir uns diesen Prozess visuell an:

1. Der Webbrowser lädt index.html
2. In index.html gibt es ein div mit id="app"
3. main.js wird ausgeführt und erstellt die Vue-Anwendung
4. Die Vue-Anwendung wird am div mit id="app" angehängt
5. App.vue wird gerendert und alle verschachtelten Komponenten werden geladen

## Zusammenfassung

Du solltest jetzt verstehen, wie wir ein Vue-Projekt erstellen können und wie wir es über die Vue UI verwalten können. Wir haben auch das für uns erstellte Projekt erkundet, um uns auf die Anpassung dieses Projekts vorzubereiten. In der nächsten Lektion werden wir unsere erste Single-File .vue-Komponente erstellen.