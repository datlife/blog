# Personal site with Hugo

## Prerequistes

* Hugo (https://gohugo.io/installation/macos/)
```
brew install hugo
```
* (optional) when running on new machines, themes need to be reinit again as submodule
   - ensure ssh agent and key setup `ssh -T git@github.com`
   - make sure .gitsubmodules has correct paths
   - run `git submodule update`
## Dev

* start dev server locally
```
hugo server -D
```

## Add a new post

## Add a new page

## Publish

```
./deploy.sh "add new post"
```