# Data
This folder is for data associated with your project for **local use only**.

Some key ideas to keep in mind:
* You really should **never commit your data to git/GitHub**
* Data belongs in a sensible storage solution, like a database or a storage bucket
* A repository of version-controlled code is **not a sensible storage solution for data**
* **Don't use this location for storing your data**

The reason you shouldn't commit data to your code repository, especially if it's hosted some place public like GitHub, is that your data could very well include the private information of individuals. **Individual privacy should be protected, guarded, and cherished by data science practitioners**.

After all of these statements, why even include this directory at all? Mainly, because it's useful to have a place in the project to handle local files while doing development work. **Just because something is useful while doing development work doesn't mean that it should be in your primary source code repository**.

For this reason, I've actually included `data/` in the `.gitignore` file. I'm doing my best to keep you from accidentally or cavalierly publishing data to the Web. **Be responsible with data**.