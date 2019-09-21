//
//  SnowmanViewController.swift
//  TheSeven7
//
//  Created by Ayline Villegas  on 9/21/19.
//  Copyright © 2019 Ayline Villegas . All rights reserved.
//

import UIKit
import WebKit

class SnowmanViewController: UIViewController {

    @IBOutlet weak var webView: UIWebView!
    override func viewDidLoad() {
        super.viewDidLoad()
        let url = URL(string:"https://www.cbc.ca/kidscbc2/content/games/build-your-snowman/index.html")
        let request = URLRequest(url: url!)
        webView.loadRequest(request)

        // Do any additional setup after loading the view.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
