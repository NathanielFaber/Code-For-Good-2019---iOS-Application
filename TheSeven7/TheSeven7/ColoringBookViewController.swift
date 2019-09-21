//
//  ColoringBookViewController.swift
//  TheSeven7
//
//  Created by Ayline Villegas  on 9/21/19.
//  Copyright © 2019 Ayline Villegas . All rights reserved.
//

import UIKit
import WebKit

class ColoringBookViewController: UIViewController {

    @IBOutlet weak var webView: UIWebView!
    override func viewDidLoad() {
        super.viewDidLoad()
        let url = URL(string:"https://games.cdn.famobi.com/html5games/k/kids-color-book-2/v230/?fg_domain=play.famobi.com&fg_aid=A1000-1&fg_uid=03b1e156-de50-49d6-964b-01ea276eee3d&fg_pid=4638e320-4444-4514-81c4-d80a8c662371&fg_beat=584&original_ref=https%3A%2F%2Fgames.famobi.com%2Feducational%2Fkids-color-book-2%3Ftechnology%3Dweb")
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
