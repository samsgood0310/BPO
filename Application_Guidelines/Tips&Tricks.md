
### Lines of code 
git ls-files | grep '\.py' | xargs wc -l

### Delete __pycache__ files
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
