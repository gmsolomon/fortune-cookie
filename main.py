#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random
def getrandomfortune():
    fortunes = ["You will inherit a great gift soon.", "Your finances will improve.", "A career change is in your future."]
    todays_fortune = random.choice(fortunes)
    return(todays_fortune)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header ='<h1> Fortune Cookie</h1>'
        fortune = "<strong>" + getrandomfortune() + "</strong>"
        fortune_sentence = "Your fortune is: " + fortune
        fortune_paragraph = "<p>" + fortune_sentence + "</p>"
        lucky_number = "<strong>" + str(random.randint(1,100)) +"</strong>"
        number_sentence = 'Your lucky number is: ' + lucky_number
        number_paragraph = "<p>" + number_sentence + "</p>"
        another_cookie = "<a href='.'> <button> Another cookie please! </buttong></a>"
        self.response.write( header + fortune_paragraph + number_paragraph+ another_cookie)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
