//
//  YoutubeViewController.swift
//  
//
//  Created by Sravya Patakota on 9/21/19.
//

import UIKit
import WebKit

class YoutubeViewController: UIViewController {

    @IBOutlet weak var webView: UIWebView!
    override func viewDidLoad() {
        super.viewDidLoad()
        let url = URL(string:"https://www.youtube.com/user/thechicagocac")
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
