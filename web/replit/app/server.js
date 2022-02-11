const vm = require("vm");
const http = require("http");
const repl = require("repl");
const fileSystem = require("fs");
const path = require("path");
var buf0 = new Buffer.from([0]);

const secretAgent = { 1: ["fa2y"] };
const unwantedCommands = ["editor", "load", "save", "break"];
const UNSAFE_WORDS = [
  "this",
  "constructor",
  "process",
  "binding",
  "process_wrap",
  "child_process",
  "mainModule",
  "require",
  "import",
  "toString",
  "String",
  "fs",
  "Buffer",
  "base64",
];

const unsafeWordsObj = UNSAFE_WORDS?.reduce(
  (obj, key) => ({ ...obj, [key]: "*"?.repeat(2) }),
  {}
);

const isValid = (cmd) => /^[a-z\[\]()_.\r\n\'=>]+$/?.test(cmd);

const escapeUnsafeKeywords = (cmd, obj) => {
  const reg = new RegExp(Object?.keys(obj)?.join("|"), "i");
  cmd = cmd?.replace(reg, (matched) => obj[matched]);
  return cmd;
};

const xEval = (cmd, context, filename, callback) => {
  let result;
  try {
    cmd = escapeUnsafeKeywords(cmd, unsafeWordsObj);
    if (isValid(cmd)) {
      if (cmd?.length > 15) {
        result = null;
      } else {
        result = vm?.runInThisContext(cmd);
      }
    } else {
      result = null;
    }
  } catch (e) {
    console?.log(e);
  }
  callback(null, result);
};

var server = http.createServer((req, res) => {
  res?.setHeader("X-Powered-By", "Node js Read-Eval-Print-Loop (REPL)");
  res?.setHeader("Content-Type", "multipart/octet-stream");
  res?.write("Welcome to the fun jail \r\n");

  var replServer = repl?.start({
    prompt: "$ >",
    eval: xEval,
    input: req,
    output: res,
    terminal: false,
    useColors: true,
    useGlobal: false,
  });

  // delete unwanted commands
  for (var cmd in unwantedCommands) {
    delete replServer?.commands[cmd];
  }
  // delete context globals
  for (var key in replServer?.context) {
    delete replServer?.context[key];
  }

  replServer?.defineCommand("getSource", {
    help: "get the source code",
    action() {
      try {
        const filePath = path?.join(__dirname, "server.js");
        const data = fileSystem?.readFileSync(filePath, "utf8");
        res?.write(data);
      } catch (e) {
        console.log(e);
      }
    },
  });

  replServer?.defineCommand("getFlag", {
    help: "get your flag",
    action() {
      try {
        if (secretAgent[1]?.toString() === "vvxhid") { // how ?
          res?.write(`Here is the Flag ${process?.env?.FLAG}`);
        }
      } catch (e) {}
      replServer?.clearBufferedCommand();
      replServer?.close();
      res?.end();
      // exit?
      process.exit()
    },
  });

  var iv = setInterval(() => {
    res?.write(buf0);
  }, 100);

  res?.connection?.on("end", () => {
    clearInterval(iv);
  });
});
// listening
server?.listen(8080);
