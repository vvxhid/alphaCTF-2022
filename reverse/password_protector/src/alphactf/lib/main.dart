import 'package:alphactf/safe.dart';
import 'package:flutter/material.dart';
import 'dart:math';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      debugShowMaterialGrid: false,
      title: 'My first Password Saver',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'My first Password Saver'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final FocusNode passwordFocusNode = FocusNode();
  late String password;
  final TextEditingController _passwordController = TextEditingController();
  @override
  void initState() {
    password = getRandomString(64);
    super.initState();
  }

  void _checkPassword() {
    passwordFocusNode.unfocus();
    if (_passwordController.text == password) {
      Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => Safe()),
      );
    } else {
      setState(() {
        password = getRandomString(64);
        _passwordController.text = '';
      });
      var snackBar = const SnackBar(
          content:
              Text("Nah, that's wrong LOL \nA new password is generated."));
      ScaffoldMessenger.of(context).showSnackBar(snackBar);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Text(
                'What is the secret key ?',
                style: Theme.of(context).textTheme.headline3,
                textAlign: TextAlign.center,
              ),
              Padding(
                padding: const EdgeInsets.only(top: 20.0, bottom: 20.0),
                child: TextField(
                  controller: _passwordController,
                  focusNode: passwordFocusNode,
                  obscureText: true,
                  enableSuggestions: false,
                  autocorrect: false,
                  decoration: const InputDecoration(
                    filled: true,
                    fillColor: Colors.white,
                    labelText: "Password",
                    hintText: "Password",
                    prefixIcon: Icon(Icons.lock),
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.all(
                        Radius.circular(25.0),
                      ),
                    ),
                  ),
                ),
              ),
              Text(
                'The password is a 64 random character, and each time you fail, a new password is generated\n Good Luck :)',
                style: Theme.of(context).textTheme.subtitle1,
                textAlign: TextAlign.center,
              ),
            ],
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: _checkPassword,
        tooltip: 'Increment',
        label: const Text("Check Password"),
        icon: const Icon(Icons.arrow_forward),
      ),
    );
  }
}

const _chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890';
Random _rnd = Random();

String getRandomString(int length) => String.fromCharCodes(Iterable.generate(
    length, (_) => _chars.codeUnitAt(_rnd.nextInt(_chars.length))));
