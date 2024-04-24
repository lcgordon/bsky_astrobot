import { createRequire } from 'module'

export default async function getPostText() {
  const require = createRequire(import.meta.url)
  // Generate the text for your post here. You can return a string or a promise that resolves to a string
  
  // start my code
  // const child_process = require("child_process");//.spawnSync;
  // const pythonProcess = child_process.spawnSync('python',["./arxivapi.py"]);

  //https://stackoverflow.com/questions/14332721/node-js-spawn-child-process-and-get-terminal-output-live
  var child_process = require('child_process');

  var child = child_process.spawnSync("python", ["./arxivapi.py"], { encoding : 'utf8' });
  console.log("Process finished.");
  if(child.error) {
      console.log("ERROR: ",child.error);
  }
  // console.log("stdout: ",child.stdout);
  // console.log("stderr: ",child.stderr);
  // console.log("exist code: ",child.status);
  return child.stdout;


  // pythonProcess.stdout.on('data', (data:any) => {
  //   // Do something with the data returned from python script
  //   console.log(`${data.toString()}`);
  //  });

  //  var scriptOutput = "";

  //   // pythonProcess.stdout.setEncoding('utf8');
  //   pythonProcess.stdout.on('data', function(data:any) {
  //       console.log('stdout: ' + data);

  //       data=data.toString();
  //       scriptOutput+=data;
  //   });
  //   console.log(`${scriptOutput}`);

    // pythonProcess.on('close', function(code) {
    //   callback(scriptOutput,code);
    //  });


  // return "THIS IS A BOT TEST POST!";

}
