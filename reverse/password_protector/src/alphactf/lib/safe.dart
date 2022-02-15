import 'package:flutter/material.dart';

class Safe extends StatefulWidget {
  @override
  State<Safe> createState() => _SafeState();
}

class _SafeState extends State<Safe> {
  List<int> by73L157 = [
    1400,
    1365,
    1353,
    1361,
    1368,
    1402,
    1389,
    1407,
    1346,
    1367,
    1290,
    1359,
    1290,
    1355,
    1382,
    1292,
    1361,
    1293,
    1355,
    1290,
    1382,
    1293,
    1367,
    1382,
    1293,
    1353,
    1353,
    1382,
    1288,
    1367,
    1382,
    1373,
    1290,
    1371,
    1356,
    1280,
    1382,
    1364,
    1289,
    1373,
    1290,
    1348
  ];
  late String fl4g;
  @override
  void initState() {
    fl4g = '';
    for (int i = 0; i < by73L157.length; i++) {
      fl4g = fl4g + String.fromCharCode(by73L157[i] ^ 1337);
    }
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Here is your reward"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Center(
          child: Text(
            fl4g,
          ),
        ),
      ),
    );
  }
}
