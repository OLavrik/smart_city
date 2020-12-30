# SmartCity frontend

## To start development

### Install dependencies
```shell script
npm install
```


### Run dev server locally:

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

```shell script
npm start
```


## Build to a static files

When You are ready to publish your work to Produciton, build a bundle:

Ensure `.env` file exists and points to a proper API URL.

```shell script
npm run build
```
Check complied site at `build/` folder. Copy it to your server and serve with static server



### Serve a build
Install minimalistic statics server
```
npm install serve
```

Run it
```shell
npx serve -s build -l 5080
```