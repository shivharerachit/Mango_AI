import 'dart:convert';

import 'package:http/http.dart' as http;

Future<String> qna(String content) async {
  String endpoint = "https://mangocloud-2b2gpae35q-uc.a.run.app/mango/qna";
  try {
    print("This code is running 1");
    final url = Uri.parse(endpoint);
    Map<String, dynamic> mp = {
      "user_id": "12345",
      "question": content,
      "chat_history": []
    };
    final respose = await http.post(url,
        headers: {'Content-Type': 'application/json'}, body: jsonEncode(mp));
    print("Result is found");
    var body = jsonDecode(respose.body);
    print(body["answer"]);
    return body["answer"];
  } catch (err) {
    print(err);
    return "";
  }
}
