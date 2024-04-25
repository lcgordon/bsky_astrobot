import { createRequire } from 'module' //https://stackoverflow.com/questions/55997921/how-do-i-change-these-require-statements-for-these-modules-to-use-import-stateme

export default async function getPostText() {
  const require = createRequire(import.meta.url)
  // Generate the text for your post here. You can return a string or a promise that resolves to a string
  //https://stackoverflow.com/questions/23450534/how-to-call-a-python-function-from-node-js
  //https://stackoverflow.com/questions/14332721/node-js-spawn-child-process-and-get-terminal-output-live
  var child_process = require('child_process');

  var child = child_process.spawnSync("python", ["arxivapi.py"], { encoding : 'utf8' });
  console.log("Process finished.");
  console.log(child.stdout);
  if(child.error) {
      console.log("ERROR: ",child.error);
  }
  return child.stdout; 

}
