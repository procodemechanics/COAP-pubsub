diff --git a/broker.cpp b/broker.cpp
index 21c82dc..9fb11a0 100644
--- a/broker.cpp
+++ b/broker.cpp
@@ -26,6 +26,9 @@
 #define GC_TIMEOUT 1
 #define MAX_AGE_DEFAULT 60
 
+#define MAX_TOPIC 10
+static int topic_count;
+
 /* Testing
 coap get "coap://127.0.0.1:5683/.well-known/core?ct=0&rt=temperature"
 coap get "coap://127.0.0.1:5683/.well-known/core?rt=temperature&ct=1"
@@ -487,7 +490,9 @@ CoapPDU::Code get_handler(Resource* resource, CoapPDU* pdu, struct sockaddr_in*
 CoapPDU::Code post_create_handler(Resource* resource, const char* in, char* &payload, struct yuarel_param* queries, int num_queries) {
     if (resource->ct != CoapPDU::COAP_CONTENT_FORMAT_APP_LINK)
         return CoapPDU::COAP_BAD_REQUEST;
-    
+    if( topic_count == MAX_TOPIC)
+        return CoapPDU::COAP_FORBIDDEN;
+
     char * p = (char *) strchr(in, '<');
     int start = (int)(p-in);
     p = (char *) strchr(in, '>');
@@ -543,6 +548,7 @@ CoapPDU::Code post_create_handler(Resource* resource, const char* in, char* &pay
     new_resource->subs = NULL;
     payload = resource_uri;
     // update_discovery(discover);
+    topic_count = topic_count + 1;
     return CoapPDU::COAP_CREATED;
 }
 
@@ -665,6 +671,7 @@ CoapPDU::Code delete_remove_handler(Resource* resource, Resource* parent, Resour
     }*/
     
     remove_all_resources(resource, true, parent, prev, sockfd, addrLen);
+    topic_count = topic_count - 1;
     return CoapPDU::COAP_DELETED;
 }
 
